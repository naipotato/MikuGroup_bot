import { Composer } from 'telegraf';

const DeleteMessages = new Composer();

DeleteMessages.command('del', async ctx => {
	if (ctx.message!.reply_to_message == undefined) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Ehm... No respondiste al mensaje que debo borrar', { reply_to_message_id: ctx.message!.message_id });
		return;
	}

	let chatMember = await ctx.getChatMember(ctx.from!.id);
	if (!chatMember.can_delete_messages && chatMember.status != 'creator') {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Lo siento, pero no estás autorizad@ para borrar mensajes.', {
			reply_to_message_id: ctx.message!.message_id
		});
		return;
	}

	chatMember = await ctx.getChatMember(ctx.botInfo?.id ?? (await ctx.tg.getMe()).id);
	if (!chatMember.can_delete_messages) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Etto... no tengo los permisos para borrar mensajes (╥_╥)', {
			reply_to_message_id: ctx.message!.message_id
		});
		return;
	}

	await ctx.deleteMessage(ctx.message!.reply_to_message.message_id);
	await ctx.deleteMessage(ctx.message!.message_id);
});

export default DeleteMessages;
