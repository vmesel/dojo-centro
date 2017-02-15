var assert = require ('assert'),
    equilibrio = require('./problem').equilibrio;

describe('equilibrio', function() {
    it('vetor vazio', function () {
        var vetor = []
        assert.equal(equilibrio(vetor), null)
    })

    it('vetor de 1 elemento', function () {
        var vetor = [1]
        assert.equal(equilibrio(vetor), 0)
    })

    it('vetor de 2 elementos segundo mais pesado', function () {
        var vetor = [1, 2]
        assert.equal(1, equilibrio(vetor))
    })

    it('vetor de 2 elementos primeiro mais pesado', function () {
        var vetor = [2, 1]
        assert.equal(0, equilibrio(vetor))
    })

  	it('vetor de 3 elementos iguais', function () {
        var vetor = [1, 1, 1]
        assert.equal(1, equilibrio(vetor))
    })

  	it('vetor de 3 elementos o primeiro mais pesado', function () {
        var vetor = [2, 1, 1]
        assert.equal(0, equilibrio(vetor))
    })

  	it('vetor de 3 elementos o ultimo mais pesado', function () {
        var vetor = [1, 1, 3]
        assert.equal(2, equilibrio(vetor))
    })

  	it('vetor de 3 elementos o meio mais pesado', function () {
        var vetor = [3, 1, 1]
        assert.equal(0, equilibrio(vetor))
    })
})