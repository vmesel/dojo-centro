exports.pulaSapo = function (alturaPulo, alturasCanos) {
	if (alturasCanos[1] > alturasCanos[0] + 1 ||
		alturasCanos[1] > alturasCanos[0] + 2 ) {

		return 'GAME OVER'
	}

    return 'YOU WIN'
};
