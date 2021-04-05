const homeTemplate = document.createElement('template')
homeTemplate.innerHTML = `
<label id="title">
    {{ title }}
</label>
`

window.customElements.define('hw-home', class HwHome extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({mode:'open'})
        this.shadowRoot.appendChild(homeTemplate.content.cloneNode(true))

        this.titleElement = this.shadowRoot.getElementById("title")
    }
    connectedCallback() {
        fetchData('/data', document).then(data => {
            this.titleElement.innerText = data.title
        })
    }
})