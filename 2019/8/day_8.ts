let fs = require('fs');

function get_puzzle_input(): string {
	try {
		return fs.readFileSync('day_8.txt', 'utf8');
	} catch (e) {
		console.log('Critical:', e.stack);
		return '';
	}
}

function process_day_8_input(data: string): Array<Array<Array<number>>> {
	let index = 0;
	let width = 25;
	let height = 6;
	let new_data = [];
	let new_layer = [];
	let new_row = [];
	while (index < data.length) {
		new_row.push(Number(data[index]));
		index += 1;
		if (new_row.length == width) {
			new_layer.push(new_row);
			new_row = [];
		}
		if (new_layer.length == height) {
			new_data.push(new_layer);
			new_layer = [];
		}
	}
	return new_data;
}

function count_digit(digit: number, data: Array<Array<number>>): number {
	let counter = 0;
	for (let i = 0; i < data.length; i++) {
		for (let j = 0; j < data[i].length; j++) {
			if (data[i][j] == digit) {
				counter += 1;
			}
		}
	}
	return counter;
}

function part_1(data: Array<Array<Array<number>>>): number {
	let layer_number = 1;
	let special_layer = 0;
	let fewest_zeroes = count_digit(0, data[special_layer]);
	while (layer_number < data.length) {
		let seen_zeroes = count_digit(0, data[layer_number]);
		if (seen_zeroes < fewest_zeroes) {
			fewest_zeroes = seen_zeroes;
			special_layer = layer_number;
		}
		layer_number += 1;
	}
	return count_digit(1, data[special_layer]) * count_digit(2, data[special_layer]);
}

function find_color(data: Array<Array<Array<number>>>, i: number, j: number): string {
	let layer = 0;
	while (layer < data.length && data[layer][i][j] == 2) {
		layer += 1;
	}
	if (layer >= data.length) {
		return '2';
	}
	return data[layer][i][j].toString();
}

function part_2(data: Array<Array<Array<number>>>) {
	let new_layer = [];
	for (let i = 0; i < 6; i++) {
		let new_row = [];
		for (let j = 0; j < 25; j++) {
			new_row.push(find_color(data, i, j));
		}
		new_layer.push(new_row);
	}
	for (let i = 0; i < new_layer.length; i++) {
		console.log(new_layer[i].join(''));
	}
}

function day_8(data: Array<Array<Array<number>>>) {
	console.log('Part 1: ' + part_1(data));
	console.log('Part 2: ');
	part_2(data);
}

//day_8(process_day_8_input('0222112222120000'));

day_8(process_day_8_input(get_puzzle_input()));
