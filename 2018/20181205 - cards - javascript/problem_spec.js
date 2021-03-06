var assert = require ('assert'),
    maxPoints = require('./problem').maxPoints;

// https://www.urionlinejudge.com.br/judge/pt/problems/view/1224

describe('Cards', function() {
    it('with cards [2,0]', function () {
        var cards = [2, 0]
        assert.equal(maxPoints(cards), 2)
    })

    it('with cards [1,0]', function () {
        var cards = [1, 0]
        assert.equal(maxPoints(cards), 1)
    })

    it('with cards [0,1]', function () {
        var cards = [0, 1]
        assert.equal(maxPoints(cards), 1)
    })

    it('with cards [1,1,1,1]', function () {
        var cards = [1, 1, 1, 1]
        assert.equal(maxPoints(cards), 2)
    })

    it('with cards [2,1,1,1]', function () {
        var cards = [2, 1, 1, 1]
        assert.equal(maxPoints(cards), 3)
    })

    it('with cards [2,1,1,2]', function () {
        var cards = [2, 1, 1, 2]
        assert.equal(maxPoints(cards), 3)
    })

    it('with cards [47,-50,-3,7]', function () {
        var cards = [47, 50, -3, 7]
        assert.equal(maxPoints(cards), 57)
    })
    
})