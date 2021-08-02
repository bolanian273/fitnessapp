const report_btn = document.getElementById('report')
const img = document.getElementById('img')
const modelBody = document.getElementById('model-body')
const reportForm = document.getElementById('report-form')
const alertBox = document.getElementById('alert-box')

const reportcn = document.getElementById('cn')
const reportName = document.getElementById('id_name')
const reportRemarks = document.getElementById('id_remarks')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(csrf)

const handleAlerts = (type, msg) => {
    alertBox.innerHTML = ` 
        <div class = "alert alert-${type}" role="alert">
            ${msg} 
        </div> 
      `
}

console.log(reportName)
console.log(reportRemarks)

console.log(report_btn)
console.log(img)

if (img) {
    report_btn.classList.remove('not-visible')
}

report_btn.addEventListener('click', ()=>{
    console.log('clicked')
    img.setAttribute('class', 'w-100')
    modelBody.prepend(img)

    console.log(img.src)

    // reportForm.addEventListener('submit', e=> {
    //     e.preventDefault()
    //     const formData = new FormData()
    //     formData.append('csrfmiddlewaretoken',csrf)
    //     formData.append('cn', reportcn.value)
    //     formData.append('name', reportName.value)
    //     formData.append('remarks', reportRemarks.value)
    //     formData.append('image', img.src)
    //
    //     $.ajax({
    //         type: 'POST',
    //         url: '/reports/save/',
    //         data: formData,
    //         success: function (response) {
    //             console.log(response)
    //             handleAlerts('success', 'Report Created')
    //             // window.location('reports/pdf')
    //             reportForm.reset()
    //         },
    //         error: function (error) {
    //             console.log(error)
    //             // handleAlerts('danger', 'Ops... something went wrong')
    //         },
    //         processData: false,
    //         contentType: false
    //     })
    //
    // })
})