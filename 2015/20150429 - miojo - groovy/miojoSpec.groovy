import spock.lang.*
import miojo

class MiojoSpec extends spock.lang.Specification {
    def "retorna o tempo minimo"() {
        expect:
	miojo.calcula(amp1, amp2) == tempo

	where:
        amp1 | amp2 | tempo
	2    | 3    | 3
	1    | 4    | 3
        5    | 2    | 5
	7    | 4    | 7
	3    | 4    | 3
        7    | 5    | 10
        8    | 5    | 8

        5    | 4    | 8
        6    | 5    | 15
        7    | 6    | 21

	
    }
}  

