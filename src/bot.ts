import Telegraf, { Context } from 'telegraf';
import Ban from './ban';
import { TOKEN } from './constants';
import DeleteMessages from './deleteMessages';
import General from './general';
import NewMembers from './newMembers';

const bot = new Telegraf(TOKEN);

// Nos aseguramos que el evento realmente tenga un mensaje
bot.use(Telegraf.filter(ctx => {
	return ctx.message != undefined;
}));

// Si el mensaje proviene de un supergrupo, continuamos.
// En caso contrario, abandonamos el chat si es posible
bot.use(async (ctx, next) => {
	const chat = ctx.chat ?? await ctx.getChat();

	if (chat.type == 'supergroup') {
		await next();
	} else if (chat.type != 'private') {
		await ctx.leaveChat();
	}
});

// Configuramos el resto de middlewares
bot.use(NewMembers);
bot.use(DeleteMessages);
bot.use(Ban);
bot.use(General);

bot.catch((err: any, ctx: Context) => {
	console.error(`Ooops, encountered an error for ${ctx.updateType}`, err);
})

bot.telegram.setWebhook('');
bot.launch();
