package main

import "testing"

func TestInterpretaEspacoVazio(t *testing.T) {
	if "" != Interpreta("") {
		t.Errorf("TestInterpretaEspacoVazio")
	}
}

func TestInterpretaPonto(t *testing.T) {
	if "0" != Interpreta(".") {
		t.Errorf("TestInterpretaPonto")
	}
}

func TestInterpretaMaisPonto(t *testing.T) {
	if "1" != Interpreta("+.") {
		t.Errorf("TestInterpretaMaisPonto")
	}
}

func TestInterpretaPontoMais(t *testing.T) {
	if "0" != Interpreta(".+") {
		t.Errorf("TestInterpretaPontoMais")
	}
}

func TestInterpretaMenos(t *testing.T) {
	if "" != Interpreta("-") {
		t.Errorf("TestInterpretaMenos")	
	}
}

func TestInterpretaMaisMaisPonto(t *testing.T) {
	if "2" != Interpreta("++.") {
		t.Errorf("TestInterpretaMaisMaisPonto")	
	}
}
