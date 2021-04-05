document.defaultView.customElements.define('hw-router', class HwRouter extends HTMLElement {
    static get observedAttributes() {
        return ['content'];
    }
    attributeChangedCallback(name, oldValue, newValue) {
        this.content = newValue
    }
    constructor() {
        super();
        this.routes = [
            { match:(request)=> request == '?page=users', html:`<hw-users></hw-users>` },
            { match:()=> true, html:`<hw-home></hw-home>` }
        ]
    }
    connectedCallback() {
        let request = window.location.search
        let app = document.getElementById(this.content)
        app.innerHTML = this.routes.find(route => route.match(request)).html
    }
})