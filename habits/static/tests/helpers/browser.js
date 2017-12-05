require('babel-register')();

const { JSDOM } = require('jsdom');
const jsdom = new JSDOM('<!doctype html><html><body></body></html>',
                        { url: "http://localhost:5000/" });
const { window } = jsdom;

var enzyme = require('enzyme');
var Adapter = require('enzyme-adapter-react-16');
enzyme.configure({ adapter: new Adapter() });

function copyProps(src, target) {
    const props = Object.getOwnPropertyNames(src)
        .filter(prop => typeof target[prop] === 'undefined')
        .reduce((result, prop) => ({
            ...result,
            [prop]: Object.getOwnPropertyDescriptor(src,prop),
        }), {});
    Object.defineProperties(target, props);
}

global.window = window
global.document = window.document;
global.navigator = {
    userAgent: 'node.js'
};

copyProps(window, global);
