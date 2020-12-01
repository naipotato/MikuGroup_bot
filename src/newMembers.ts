import { Composer, Context } from 'telegraf';
import { Message } from 'telegraf/typings/telegram-types';
import { TELEGRAM_GROUP } from './constants';

const NewMembers = new Composer();

async function addedToGroup(ctx: Context): Promise<void> {
	await ctx.replyWithChatAction('typing');
	await ctx.reply('Kon\'nichiwa, Hatsune Miku desu! ＼(≧▽≦)／');
	await ctx.replyWithSticker('CAADAgADsBsAAuCjggdzuy-p9Uzd2gI');
	await ctx.replyWithChatAction('typing');
	await ctx.reply('Estoy aquí para ayudar a los novios <a href="tg://user?id=82982166">Nahuel</a> y ' +
		'<a href="tg://user?id=359710858">Zoé</a> a administrar este increíble grupo, así que es un placer conocerlos ' +
		'(◕‿◕)', { parse_mode: 'HTML' });
}

// Filtramos que el grupo sea realmente nuestro grupo :)
NewMembers.use(async (ctx, next) => {
	const chat = ctx.chat ?? await ctx.getChat();

	if (chat.id != Number(TELEGRAM_GROUP)) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Eh? Qué hago aquí? Este no es [mi grupo](https://t.me/joinchat/BPI1Flj3XFgYwtfRm6SC-w)! (>_<)', {
			parse_mode: 'MarkdownV2',
		});
		await ctx.leaveChat();
	}

	await next();
});

// En caso de que hayan nuevos miembros, los saludamos :D
NewMembers.use(async (ctx, next) => {
	if (ctx.message!.new_chat_members == undefined) {
		// No hay nuevos miembros, seguimos de largo
		await next();
		return;
	}

	if (ctx.message!.new_chat_members.find(async value => value.id == ctx.botInfo?.id ?? (await ctx.tg.getMe()).id)) {
		// En caso de que el bot mismo haya sido añadido, dar mensaje de saludo al grupo
		await addedToGroup(ctx);
		return;
	}

	let msg: Message;
	if (ctx.message!.new_chat_members.length == 1) {
		// Hay solo 1 nuevo miembro, saludarlo personalizadamente UwU
		await ctx.replyWithChatAction('typing');
		msg = await ctx.reply(`Hola ${ctx.message!.new_chat_members[0].first_name}, bienvenid@ al grupo!`, {
			reply_to_message_id: ctx.message!.message_id,
		});
	} else {
		// Hay más de 1 miembro, saludar de forma general
		await ctx.replyWithChatAction('typing');
		msg = await ctx.reply('Hola, sean bienvenid@s!', { reply_to_message_id: ctx.message!.message_id });
	}

	// En todo caso, siempre mandar un sticker al final
	const sticker = await ctx.replyWithSticker('CAADAgADtBsAAuCjgge3gHY3V1-8zgI');

	// Y guardamos todo esto para borrarlo pasados 60 segundos
	setTimeout(async () => {
		await ctx.deleteMessage(ctx.message!.message_id);
		await ctx.deleteMessage(msg.message_id);
		await ctx.deleteMessage(sticker.message_id);
	}, 60 /* segundos */ * 1000 /* milisegundos en un segundo */);
})

export default NewMembers;
