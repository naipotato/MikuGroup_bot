import { Composer } from 'telegraf';
import { User } from 'telegraf/typings/telegram-types';

const Ban = new Composer();

Ban.command('ban', async ctx => {
	if (ctx.message!.reply_to_message == undefined) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Uhm? No puedo banear a nadie si no respondes a un mensaje', {
			reply_to_message_id: ctx.message!.message_id
		});
		return;
	}

	let chatMember = await ctx.getChatMember(ctx.from!.id);
	if (!chatMember.can_restrict_members && chatMember.status != 'creator') {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Lo siento, pero me dijeron que tú no puedes banear usuarios...');
		return;
	}

	chatMember = await ctx.getChatMember(ctx.botInfo?.id ?? (await ctx.tg.getMe()).id);
	if (!chatMember.can_restrict_members) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Etto... no tengo los permisos para banear usuarios (╥_╥)', {
			reply_to_message_id: ctx.message!.message_id
		});
		return;
	}

	let user: User;
	if (ctx.message!.reply_to_message.forward_from != undefined) {
		user = ctx.message!.reply_to_message.forward_from;
	} else {
		user = ctx.message!.reply_to_message.from!;
	}

	if (user.id == (ctx.botInfo?.id ?? (await ctx.tg.getMe()).id)) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Hey! Esa soy yo! (O.O)', { reply_to_message_id: ctx.message!.message_id });
		await ctx.replyWithSticker('CAADAgADrRsAAuCjgge1g6be76IiHgI');
		return;
	}

	if (ctx.message!.reply_to_message.forward_from != undefined) {
		chatMember = await ctx.getChatMember(ctx.message!.reply_to_message.forward_from.id);
	} else {
		chatMember = await ctx.getChatMember(ctx.message!.reply_to_message.from!.id);
	}

	if (chatMember.status == 'administrator' || chatMember.status == 'creator') {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Etto... No puedo banear administradores (⌒_⌒;)', { reply_to_message_id: ctx.message!.message_id });
		return;
	}

	if (ctx.message!.reply_to_message.forward_from != undefined) {
		ctx.kickChatMember(ctx.message!.reply_to_message.forward_from.id);
	} else {
		ctx.kickChatMember(ctx.message!.reply_to_message.from!.id);
	}

	await ctx.replyWithChatAction('typing');
	await ctx.reply('¡Banead@!', { reply_to_message_id: ctx.message!.reply_to_message.message_id });
	await ctx.replyWithSticker('CAADAgADpxsAAuCjggf0_Fu4xLzgxAI');
});

Ban.command('kick', async ctx => {
	if (ctx.message!.reply_to_message == undefined) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Uhm? No puedo expulsar a nadie si no respondes a un mensaje', {
			reply_to_message_id: ctx.message!.message_id
		});
		return;
	}

	let chatMember = await ctx.getChatMember(ctx.message!.from!.id);
	if (!chatMember.can_restrict_members && chatMember.status != 'creator') {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Lo siento, pero me dijeron que tú no puedes expulsar usuarios...', {
			reply_to_message_id: ctx.message!.message_id
		});
		return;
	}

	chatMember = await ctx.getChatMember(ctx.botInfo?.id ?? (await ctx.tg.getMe()).id);
	if (!chatMember.can_restrict_members) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Etto... no tengo los permisos para expulsar usuarios (╥_╥)', {
			reply_to_message_id: ctx.message!.message_id
		});
		return;
	}

	let user: User;
	if (ctx.message!.reply_to_message.forward_from != undefined) {
		user = ctx.message!.reply_to_message.forward_from;
	} else {
		user = ctx.message!.reply_to_message.from!;
	}

	if (user.id == (ctx.botInfo?.id ?? (await ctx.tg.getMe()).id)) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Hey! Esa soy yo! (O.O)', { reply_to_message_id: ctx.message!.message_id });
		await ctx.replyWithSticker('CAADAgADrRsAAuCjgge1g6be76IiHgI');
		return;
	}

	if (ctx.message!.reply_to_message.forward_from != undefined) {
		chatMember = await ctx.getChatMember(ctx.message!.reply_to_message.forward_from.id);
	} else {
		chatMember = await ctx.getChatMember(ctx.message!.reply_to_message.from!.id);
	}

	if (chatMember.status == 'administrator' || chatMember.status == 'creator') {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Etto... No puedo expulsar administradores (⌒_⌒;)', { reply_to_message_id: ctx.message!.message_id });
		return;
	}

	if (ctx.message!.reply_to_message.forward_from != undefined) {
		await ctx.kickChatMember(ctx.message!.reply_to_message.forward_from.id);
		await ctx.unbanChatMember(ctx.message!.reply_to_message.forward_from.id);
	} else {
		await ctx.kickChatMember(ctx.message!.reply_to_message.from!.id);
		await ctx.unbanChatMember(ctx.message!.reply_to_message.from!.id);
	}

	await ctx.replyWithChatAction('typing');
	await ctx.reply('¡Expulsad@!', { reply_to_message_id: ctx.message!.reply_to_message.message_id });
	await ctx.replyWithSticker('CAADAgADpxsAAuCjggf0_Fu4xLzgxAI');
});

Ban.command('kickme', async ctx => {
	let chatMember = await ctx.getChatMember(ctx.botInfo?.id ?? (await ctx.tg.getMe()).id);
	if (!chatMember.can_restrict_members) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Etto... no tengo los permisos para expulsar usuarios (╥_╥)', {
			reply_to_message_id: ctx.message!.message_id
		});
		return;
	}

	chatMember = await ctx.getChatMember(ctx.message!.from!.id);
	if (chatMember.status == 'administrator' || chatMember.status == 'creator') {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Etto... No puedo expulsar administradores (⌒_⌒;)', { reply_to_message_id: ctx.message!.message_id });
		return;
	}

	await ctx.kickChatMember(ctx.message!.from!.id);
	await ctx.unbanChatMember(ctx.message!.from!.id);

	await ctx.replyWithChatAction('typing');
	await ctx.reply('¡Espero que vuelvas pronto! ( ; ω ; )', { reply_to_message_id: ctx.message!.message_id });
	await ctx.replyWithSticker('CAADAgADmhsAAuCjggeKLIclx5HvGQI');
});

Ban.command('unban', async ctx => {
	if (ctx.message!.reply_to_message == undefined) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Uhm? No puedo desbanear a nadie si no respondes a un mensaje', {
			reply_to_message_id: ctx.message!.message_id
		});
		return;
	}

	let chatMember = await ctx.getChatMember(ctx.message!.from!.id);
	if (!chatMember.can_restrict_members && chatMember.status != 'creator') {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Lo siento, pero me dijeron que tú no puedes desbanear usuarios...', {
			reply_to_message_id: ctx.message!.message_id
		});
		return;
	}

	chatMember = await ctx.getChatMember(ctx.botInfo?.id ?? (await ctx.tg.getMe()).id);
	if (!chatMember.can_restrict_members) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Etto... no tengo los permisos para desbanear usuarios (╥_╥)', {
			reply_to_message_id: ctx.message!.message_id
		});
		return;
	}

	if (ctx.message!.reply_to_message.forward_from != undefined) {
		ctx.unbanChatMember(ctx.message!.reply_to_message.forward_from.id);
	} else {
		ctx.unbanChatMember(ctx.message!.reply_to_message.from!.id);
	}

	await ctx.replyWithChatAction('typing');
	await ctx.reply('¡Desbanead@! (o^▽^o)', { reply_to_message_id: ctx.message!.reply_to_message.message_id });
	await ctx.replyWithSticker('CAADAgADshsAAuCjgge9W_YhLXZXrgI');
});

export default Ban;
