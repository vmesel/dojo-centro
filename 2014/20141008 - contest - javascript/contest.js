
exports.nobodySolvedAllTheProblems = function (placar) {
    var ok = true

    for(var i = 0; ok && i < placar.length; i+= 1) {
        ok = placar[i].some(function(element) {
            return element == 0
        })
    }

    return ok
}

exports.everyProblemWasSolvedByAtLeastOnePerson = function (placar) {
    lista = []
    for(var col = 0; col < placar[0].length; col+= 1) {
        accumulatedSum = 0
        for(var lin = 0; lin < placar.length;lin += 1) {
            accumulatedSum += placar[lin][col]
        }
        lista[col] = accumulatedSum
    }

    return !lista.some(function(element) { return element == 0 })
}

exports.thereIsNoProblemSolvedByEveryone = function (placar) {
    competidores = placar.length

    lista = []
    for(var col = 0; col < placar[0].length; col+= 1) {
        accumulatedSum = 0
        for(var lin = 0; lin < competidores;lin += 1) {
            accumulatedSum += placar[lin][col]
        }
        lista[col] = accumulatedSum
    }

    return !lista.some(function(element) { return element == competidores })

}

exports.everyoneSolvedAtLeastOneProblem = function (placar) {
    var ok = true

    for(var i = 0; ok && i < placar.length; i+= 1) {
        ok = placar[i].some(function(element) {
            return element == 1
        })
    }

    return ok
}

exports.contest = function (placar) {

    var somatorio = 0
    if(exports.nobodySolvedAllTheProblems(placar)) {
        somatorio += 1
    }
    if(exports.everyProblemWasSolvedByAtLeastOnePerson(placar)) {
        somatorio += 1
    }
    if(exports.thereIsNoProblemSolvedByEveryone(placar)) {
        somatorio += 1
    }
    if(exports.everyoneSolvedAtLeastOneProblem(placar)) {
        somatorio += 1
    }

    return somatorio
}
