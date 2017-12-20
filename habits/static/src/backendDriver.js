export const postHabit = (json, successCallback, failureCallback) => {
    const request = new XMLHttpRequest()
    request.open('POST', '/habits/')
    request.setRequestHeader('Content-Type', 'application/json')
    request.onload = event => {
        const response = JSON.parse(request.responseText)
        if (request.status === 201) {
            successCallback(response)
        } else if (failureCallback) {
            failureCallback(request, response)
        }
    }
    request.send(JSON.stringify(json))
}

export const requestToDeleteHabit = (id, successCallback, failureCallback) => {
    const request = new XMLHttpRequest()
    request.open('DELETE', '/habits/' + id)
    request.onload = event => {
        const response = JSON.parse(request.responseText)
        if (request.status === 200) {
            successCallback(response)
        } else if (failureCallback) {
            failureCallback(request, response)
        }
    }
    request.send(null)
}
