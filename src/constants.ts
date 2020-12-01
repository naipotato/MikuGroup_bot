import { config } from 'dotenv';

if (process.env.NODE_ENV == 'development') {
	const result = config();

	if (result.error) {
		console.error(`Error: ${result.error.message}`);
		process.exit(1);
	}
}

if (!process.env.TOKEN) {
	console.error('Error: TOKEN is not defined');
	process.exit(1);
}

export const TOKEN = process.env.TOKEN;

if (!process.env.TELEGRAM_GROUP) {
	console.error('Error: TELEGRAM_GROUP is not defined');
	process.exit(1);
}

export const TELEGRAM_GROUP = process.env.TELEGRAM_GROUP;
