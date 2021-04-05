const usersTemplate = document.createElement('template')
usersTemplate.innerHTML = `
<ol id="users"></ol>
`
const userTemplate = document.createElement('template')
userTemplate.innerHTML = `
<li class="user"></li>
`

document.defaultView.customElements.define('hw-users', class HwUsers extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({mode:'open'})
        this.shadowRoot.appendChild(usersTemplate.content.cloneNode(true))

        this.usersElement = this.shadowRoot.getElementById("users")
    }
    connectedCallback() {
        fetchData('/users', document).then(list => {
            list.entries.forEach( entry => {
                let cloned = userTemplate.content.cloneNode(true)
                let userElement = cloned.querySelector('.user')
                userElement.id = entry.id
                userElement.innerHTML = entry.username
                this.usersElement.appendChild(cloned)
            })
        })
    }
})