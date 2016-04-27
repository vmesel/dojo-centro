// https://www.urionlinejudge.com.br/judge/en/problems/view/1426
import spock.lang.*
import static brickOnTheWall.completeWall 

class brickOnTheWallSpec extends spock.lang.Specification {
    def "test"() {
        expect:
        completeWall(filled) == result

        where:
        filled           | result
        [4,1,1]          | [4,2,2,1,1,1]
        [2,0,0]          | [2,1,1,0,1,0]
    }
}