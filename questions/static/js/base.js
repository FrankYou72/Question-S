const baseUrl = 'http://127.0.0.1:8000'

let customList = []

async function updateThemes() {

    const themeSelect = document.getElementById('themeSelect')
    themeSelect.innerHTML = ''
    const area = document.getElementById('areaSelect').value

    let emptyOpt = document.createElement('option')
    emptyOpt.innerHTML = ''
    themeSelect.appendChild(emptyOpt) 

    if (area !== ''){

        let decodedArea = decodeURI(area)
        console.log(decodedArea)
        let url = `${baseUrl}/api/question_models/?area=${decodedArea}`
        const body = {
            method: 'GET',
            headers: {
                "Content-Type": "application/json",
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
                //console.log(themeList)
            })
        })
    }

    

}

function makeList(){

    const customOl = document.getElementById('customOl')
    const customDisplay = document.getElementsByClassName('customDisplay')
    const theme = document.getElementById('themeSelect').value
    const area = document.getElementById('areaSelect').value

    let item = document.createElement('li')
    item.innerHTML = `${theme} - ${area}`
    customOl.appendChild(item)

    customList.push({
        "area": decodeURI(area),
        "theme": decodeURI(theme)
    })

    customDisplay.style.display = "block"

}

async function sendList() {

    let url = `${baseUrl}/api/custom/`
    const returnList = {
        questions: [],
        answers: []
    }
    const body = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            'modelList': customList
        })
    }
    fetch(url, body).then(
        response => {
            console.log(response.clone().json())
            return response.json()
        }
    ).then(
        result => {
            //console.log(result)
            //window.location.href = `${baseUrl}/custom/show`
            const questions = result['questions']
            const answers = result['answers']
            const customQuestions = document.getElementById('customQuestions')
            const customAnswers = document.getElementById('customAnswers')
   
            questions.map(
                q => {
                    let liQuestion = document.createElement('li')
                    liQuestion.innerHTML = q
                    customQuestions.appendChild(liQuestion)

                }
            )

            answers.map(
                a => {
                    let liAnswer = document.createElement('li')
                    liAnswer.innerHTML = a
                    customAnswers.appendChild(liAnswer)
                }
            )
        }
    )
    customList = []
    const customOl = document.getElementById('customOl')
    customOl.innerHTML = ''
}