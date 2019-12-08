let fs = require('fs');

function get_puzzle_input(): string {
	try {
		return fs.readFileSync('day_8.txt', 'utf8');
	} catch (e) {
		console.log('Critical:', e.stack);
		return '';
	}
}

function process_day_8_input(data: string): string {
	return data;
}

function part_1(data: string): string {
	return 'Not Implemented';
}

function part_2(data: string): string {
	return 'Not Implemented';
}

function day_8(data: string) {
	console.log('Part 1: ' + part_1(data));
	console.log('Part 2: ' + part_2(data));
}

day_8(process_day_8_input(get_puzzle_input()));
