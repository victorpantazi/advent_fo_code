let fs = require('fs');

function get_puzzle_input(): string {
	try {
		return fs.readFileSync('day_9.txt', 'utf8');
	} catch (e) {
		console.log('Critical:', e.stack);
		return '';
	}
}

function process_day_9_input(data: string): string {
	let new_data = data;
	return new_data;
}

function part_1(data: string): string {
	return 'Not Implemented';
}

function part_2(data: string): string {
	return 'Not Implemented';
}

function day_9(data: string) {
	console.log('Part 1: ' + part_1(data));
	console.log('Part 2: ' + part_2(data));
}

day_9(process_day_9_input('test'));

day_9(process_day_9_input(get_puzzle_input()));
