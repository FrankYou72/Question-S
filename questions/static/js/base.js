const baseUrl = 'http://127.0.0.1:8000'

async function updateThemes() {

    const themeSelect = document.getElementById('themeSelect')
    themeSelect.innerHTML = ''
    const area = document.getElementById('areaSelect').value

    let decodedArea = decodeURI(area)
    console.log(decodedArea)
    let url = `${baseUrl}/api/question_models/?area=${decodedArea}`
    const body = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin':'*'
        },
    }
    let themeList = new Array()
    fetch(url).then(response => {
        return response.json()
    }).then( result => {
        let themeList = new Array()
        result.map(r => {
            themeList.push(r['tema'])
        })
        return themeList   
    }).then( themeList => {
        themeList.map(t => {
            let opt = document.createElement('option')
            opt.innerHTML = t
            themeSelect.appendChild(opt) 
        })
    })
    console.log(themeList)

}


//function updateThemes() {
//    const themeSelect = document.getElementById('themeSelect')
//    themeSelect.innerHTML = ''
//    const area = document.getElementById('areaSelect').value
//
//    let themes = getThemes(area.toString())
//
//
//    themes.map(t => {
//
//        if (t.area === area.toString()) {
//            let opt = document.createElement('option')
//            opt.innerHTML = t
//            themeSelect.appendChild(opt)
//        }
//    }
//    )}