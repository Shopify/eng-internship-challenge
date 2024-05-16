const { exec } = require("child_process");

describe('solution.js script', () => {
    it('should output correct answer to the console', (done) => {
        exec("node solution.js", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"); // trim to remove any extra newlines that console.log might generate
            done(); // indicate that this async test is complete
        });
    });
});
