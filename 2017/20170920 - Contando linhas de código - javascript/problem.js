exports.countCode = function (fileContent) {
	var lines = fileContent.split("\n")
	var ok = 1

	return lines.reduce(function(count, line) {
		line = line.trim()

		if (line.includes("/*") && !line.includes("*/")) {
			ok = 0
		}

		if (line.includes("*/")) {
			ok = 1
		}

		if (line.length > 0 
			&& !line.startsWith("//")
			){

			return count + ok 
		} else {
			return count
		}
	}, 0)
};
