const baseUrl = 'http://127.0.0.1:8000'

async function getThemes(area) {
        let url = `${baseUrl}/api/question_models/?=${area}`
        const body = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin':'*'
            },
        }
        return fetch(url).then(
            query => {
                console.log(query)
                let themeList = []
                query.map( q => {
                    themeList.push(q['tema'])
                })
                console.log(themeList)
                return themeList
            }
        )
}

function updateThemes() {
    const themeSelect = document.getElementById('themeSelect')
    const area = document.getElementById('areaSelect').value

    let themes = getThemes(area.toString())


    themes.map(t => {

        if (t.area === area.toString()) {
            let opt = document.createElement('option')
            opt.innerHTML = t
            themeSelect.appendChild(opt)
        }
    }
    )

}