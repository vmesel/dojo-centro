def division_of_nlogonia division, points
  if points[0][0] > 0 && points[0][1] > 0
    return ['NE']
  end

  if points[0][1] < 0 && points[0][0] > 0
  	return ['SE']
  end

  if points[0][0] < 0 && points[0][1] < 0
  	return ['SO']
  end
	if points[0][0] < 0 && points[0][1] > 0
  	return ['NO']
  end
  return ['divisa']
end