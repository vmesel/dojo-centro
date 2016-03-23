//https://www.hackerrank.com/challenges/even-tree
//vertices 2 <= N <= 100

var assert = require ('assert'),
    evenTree = require('./eventree').evenTree

describe('evenTree', function() {
    it('2 vertices', function () {
        var edges = [
            [1, 2]
        ]
        assert.equal(evenTree(edges), 0)
    })

    it('4 vertices, line', function () {
        var edges = [
            [1, 2],
            [2, 3],
            [3, 4]
        ]
        assert.equal(evenTree(edges), 1)
    })
})
