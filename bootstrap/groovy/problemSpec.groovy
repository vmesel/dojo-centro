import spock.lang.*
import problem

class ProblemSpec extends spock.lang.Specification {
    def "test"() {
        expect:
        problem.problem(input) == output

        where:
        input  |  output
    }
}
