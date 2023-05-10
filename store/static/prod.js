const pagination = document.querySelector(".pagination");
const pages = pagination.querySelectorAll("a");
const productList = document.querySelector(".product-list");
const products = productList.querySelectorAll("li");
const productsPerPage = 6;

function showPage(pageNumber) {
  const startIndex = (pageNumber - 1) * productsPerPage;
  const endIndex = startIndex + productsPerPage;
  for (let i = 0; i < products.length; i++) {
    if (i >= startIndex && i < endIndex) {
      products[i].style.display = "block";
    } else {
      products[i].style.display = "none";
    }
  }
}

showPage(1); // Show the first page by default

for (let i = 0; i < pages.length; i++) {
  pages[i].addEventListener("click", function (event) {
    event.preventDefault();
    const pageNumber = parseInt(this.textContent);
    showPage(pageNumber);
    for (let i = 0; i < pages.length; i++) {
      pages[i].classList.remove("active");
    }
    this.classList.add("active");
  });
}
