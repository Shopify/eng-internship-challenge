import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

describe('solution.ts output', () => {
  it('should print the correct output to the console', async () => {
    const { stdout } = await execAsync('ts-node solution.ts');

    const expected = 'HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA';
    expect(stdout.trim()).toBe(expected);
  });
});
