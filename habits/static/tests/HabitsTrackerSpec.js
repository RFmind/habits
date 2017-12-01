var assert = require('assert');

describe('The Habits Tracker', function() {
    it('should show it works', function () {
        browser.url('http://localhost:5000');
        var title = browser.getTitle();
        assert.equal(title, 'Habits Project');
    });
});
