const menuTemplate = document.createElement('template')
menuTemplate.innerHTML = `
<link  href="/css/bootstrap.css" rel="StyleSheet" type="text/css">

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">HelloWorld</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-item nav-link active" href="?page=home">Home</a>
      <a class="nav-item nav-link" href="?page=users">Users</a>
    </div>
  </div>
</nav>
`

document.defaultView.customElements.define('hw-menu', class HwMenu extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({mode:'open'})
        this.shadowRoot.appendChild(menuTemplate.content.cloneNode(true))
    }
    connectedCallback() {
        let request = window.location.search
        let links = this.shadowRoot.querySelectorAll('.nav-item')
        links.forEach(link => {
            link.classList.remove('active')
            if (link.href.includes(request)) {
                link.classList.add('active')
            }
        })
    }
})