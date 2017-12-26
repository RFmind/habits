const serverRequest = (successStatus, successCallback, failureCallback) => {
    const req = new XMLHttpRequest()
    req.onload = event => {
        const response = JSON.parse(req.responseText)
        if (req.status === successStatus) {
            successCallback(response)
        } else if (failureCallback) {
            failureCallback(response, req)
        }
    }
    return req
}

export const postHabit = (json, successCallback, failureCallback) => {
    const request = serverRequest(201, successCallback, failureCallback)
    request.open('POST', '/habits/')
    request.setRequestHeader('Content-Type', 'application/json')
    request.send(JSON.stringify(json))
}

export const requestToDeleteHabit = (id, successCallback, failureCallback) => {
    const request = serverRequest(200, successCallback, failureCallback)
    request.open('DELETE', '/habits/' + id)
    request.send()
}

export const triggerHabit = (id, successCallback, failureCallback) => {
    const request = serverRequest(200, successCallback, failureCallback)
    request.open('GET', '/habits/' + id + '/trigger/')
    request.send()
}
