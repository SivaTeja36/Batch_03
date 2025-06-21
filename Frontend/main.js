// This is the main JavaScript file for the product management web application.
(async () => {
  const res = await fetch("http://localhost:5000/api/check-auth", {credentials:"include"}); // checks whether the user is logged in or not
  if (!res.ok || !(await res.json()).auth) window.location.href = "login.html";// if not logged in , it will redirect to login pa
})();

let prods = [], filtered = [], page = 1, per = 6;    // list of products 
const tbl = document.getElementById("tbl"), cat = document.getElementById("cat"),
      minF = document.getElementById("minPrice"), maxF = document.getElementById("maxPrice"),
      info = document.getElementById("info");

document.getElementById("logoutBtn").onclick = async () => { // when the user clicks on logout button, it will log out.
  await fetch("http://localhost:5000/api/logout",{credentials:"include"});
  window.location.href="login.html"; // redirects to login page
};

document.getElementById("scrapeBtn").onclick = async () => { // when the user clicks on scrape button, it will scrape the products from the website.
  const r = await fetch("http://localhost:5000/api/scrape",{credentials:"include"}); // fetches the products from the backend
  prods = await r.json();
  cat.innerHTML = `<option></option>${[...new Set(prods.map(p=>p.category))].map(c=>`<option>${c}</option>`).join('')}`; //
  page = 1; apply();
};

cat.onchange = minF.oninput = maxF.oninput = () => { page = 1; apply(); }; // when the user changes the category or price, it will apply the filters and show the products.
function apply() { // applies the filters to the products
  const min = parseFloat(minF.value)||0, max = parseFloat(maxF.value)||Infinity, c = cat.value;
  filtered = prods.filter(p=>p.price>=min && p.price<=max && (!c || p.category===c));
  show(); // shows the filtered products
}

function show() { // displays the products in the table 
  const total = filtered.length, pages = Math.ceil(total/per); // 
  page = Math.min(Math.max(page,1),pages); //
  const sel = filtered.slice((page-1)*per,(page)*per); // selects the products to be displayed on the current page 
  tbl.innerHTML = sel.map(p=>`
    <tr>
      <td class="px-2 py-1"><img src="${p.image}" class="w-12 h-12 object-contain"/></td>
      <td class="px-2 py-1">${p.title}</td><td class="px-2 py-1">${p.category}</td>
      <td class="px-2 py-1">₹${p.price.toFixed(2)}</td>
    </tr>`).join('');
  info.textContent = `Page ${page} of ${pages}`; // shows the current page and total pages 
}

document.getElementById("prev").onclick = ()=>{ page--; show(); }; // when the user clicks on previous button, it will go to the previous page 
document.getElementById("next").onclick = ()=>{ page++; show(); }; // when the user clicks on next button, it will go to the next page 

document.getElementById("exportBtn").onclick = () => { // when the user clicks on export button, it will export the products as a CSV file 
  let csv = `"Title","Category","Price"\n` + filtered.map(p=>`"${p.title}",${p.category},${p.price}`).join("\n");
  const a = document.createElement("a");// 
  a.href=URL.createObjectURL(new Blob([csv], {type:"text/csv"})); //
  a.download="products.csv"; // creates a link to download the CSV file 
  a.click(); // 
};
