package main

import (
	"os/exec"
	"strings"
	"testing"
)

func TestSolutionOutput(t *testing.T) {
	cmd := exec.Command("go", "run", "solution.go")
	outputBytes, err := cmd.CombinedOutput()
	if err != nil {
		t.Fatalf("Failed to run the command: %v", err)
	}

	// Trim space from output and expected value
	output := strings.TrimSpace(string(outputBytes))
	expected := strings.TrimSpace("HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA")

	if output != expected {
		t.Errorf("Unexpected output, got: %q, want: %q", output, expected)
	}
}
