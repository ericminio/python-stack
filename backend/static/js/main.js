const fetchData = async (uri, document) => {
    return new Promise((resolve, reject) => {
        document.defaultView.fetch('http://localhost:5000' + uri).then(async response => {
            console.log(response)
            let data = await response.json()
            console.log(data)
            resolve(data)            
        })
    })
}