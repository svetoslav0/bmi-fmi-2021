export function removeUndefinedProps(obj) {
    for (let prop in obj) {
        if (obj.hasOwnProperty(prop) && (obj[prop] === undefined || obj[prop] === null)) {
            delete obj[prop];
        }
    }
}
