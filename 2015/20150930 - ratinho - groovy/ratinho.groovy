def static testeDeDna(pai1, pai2, filho) {

	if (pai1[1][0] == pai2[1][0] || 
	   ( pai1[1].length() > 1 && pai1[1][1] == pai2[1][1]))
			return 'CADIM'
	if (pai1[1] == filho)
		return pai1[0]

	pai1[1]==filho?pai1[0]:(pai2[1]==filho?pai2[0]:'CADIM')

}