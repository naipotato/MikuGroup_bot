import { Composer } from 'telegraf';
const Telegraf = require('telegraf');

const General = new Composer();

General.command('about', async ctx => {
	let acerca = `<b>Hatsune Miku</b> @MikuGroup_bot

<i>Un excelente bot desarrollado para administrar el grupo <a href="https://t.me/joinchat/BPI1Flj3XFgYwtfRm6SC-w">Miku Group</a>, además de tener muchos comandos divertidos :D</i>

<b>Desarrollado por:</b> <a href="tg://user?id=82982166">ナウエル 💍</a>
<b>Código fuente:</b> https://github.com/nahuelwexd/MikuGroup_bot`

	await ctx.replyWithChatAction('typing');
	await ctx.reply(acerca, {
		parse_mode: 'HTML',
		reply_to_message_id: ctx.message!.message_id,
		disable_web_page_preview: true
	});
});

General.help(async ctx => {
	let ayuda = `Estos son los comandos que puedes usar conmigo  ﾞ(˘ᵕ˘)

- <code>/ban</code> (por respuesta): banearé al usuario que respondiste, incluso si el mensaje fue reenviado.
- <code>/del</code> (por respuesta): borraré el mensaje al que respondiste.
- <code>/kick</code> (por respuesta): expulsaré al usuario, pero dejaré que pueda volver a entrar.
- <code>/kickme</code>: te expulsaré del grupo, pero podrás volver a entrar.
- <code>/pin</code> (por respuesta): anclaré el mensaje notificando a todos.
- <code>/pinmute</code> (por respuesta): anclaré el mensaje silenciosamente.
- <code>/unban</code> (por respuesta): le quitaré el ban al usuario al que respondiste, incluso si el mensaje es reenviado.
- <code>/di</code>: repetiré lo que has dicho.`

	await ctx.replyWithChatAction('typing');
	await ctx.reply(ayuda, { parse_mode: 'HTML', reply_to_message_id: ctx.message!.message_id });
});

General.command('love', Telegraf.acl([82982166, 359710858], async (ctx: any) => {
	await ctx.replyWithChatAction('typing');
	await ctx.reply('La pareja más hermosa que he conocido son [Zoé](tg://user?id=359710858) y [Nahuel](tg://user?id=82982166) ' +
		':3\n\nEsos dos tortolitos enamorados se aman incondicionalmente, se acompañan en todo lo que pueden, y anteponen ' +
		'siempre las necesidades del otro ❤️', { parse_mode: 'MarkdownV2', reply_to_message_id: ctx.message!.message_id });
	await ctx.replyWithSticker('CAADAQADwQEAAuWyyh3shINoW9G1fwI');
}));

General.command('pin', async ctx => {
	if (ctx.message!.reply_to_message == undefined) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Emm... Qué mensaje debo anclar? (・・ ) ?', { reply_to_message_id: ctx.message?.message_id });
		return;
	}

	let chatMember = await ctx.getChatMember(ctx.message!.from!.id);
	if (!chatMember.can_pin_messages && chatMember.status != 'creator') {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Tú no puedes anclar mensajes', { reply_to_message_id: ctx.message!.message_id });
		await ctx.replyWithSticker('CAADAgADoRsAAuCjggfsFEp1hLA7RQI');
		return;
	}

	chatMember = await ctx.getChatMember(ctx.botInfo?.id ?? (await ctx.tg.getMe()).id);
	if (!chatMember.can_pin_messages) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('No tengo permisos para anclar mensajes (T_T)', { reply_to_message_id: ctx.message!.message_id });
		return;
	}

	await ctx.pinChatMessage(ctx.message!.reply_to_message.message_id);

	await ctx.replyWithChatAction('typing');
	await ctx.reply('Anclado <(￣︶￣)>', { reply_to_message_id: ctx.message!.reply_to_message.message_id });
});

General.command('pinmute', async ctx => {
	if (ctx.message!.reply_to_message == undefined) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Emm... Qué mensaje debo anclar? (・・ ) ?', { reply_to_message_id: ctx.message?.message_id });
		return;
	}

	let chatMember = await ctx.getChatMember(ctx.message!.from!.id);
	if (!chatMember.can_pin_messages && chatMember.status != 'creator') {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Tú no puedes anclar mensajes', { reply_to_message_id: ctx.message!.message_id });
		await ctx.replyWithSticker('CAADAgADoRsAAuCjggfsFEp1hLA7RQI');
		return;
	}

	chatMember = await ctx.getChatMember(ctx.botInfo?.id ?? (await ctx.tg.getMe()).id);
	if (!chatMember.can_pin_messages) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('No tengo permisos para anclar mensajes (T_T)', { reply_to_message_id: ctx.message!.message_id });
		return;
	}

	await ctx.pinChatMessage(ctx.message!.reply_to_message.message_id, { disable_notification: true });

	await ctx.replyWithChatAction('typing');
	await ctx.reply('Anclado <(￣︶￣)>', { reply_to_message_id: ctx.message!.reply_to_message.message_id });
});

General.command('di', async ctx => {
	let [_, ...args] = ctx.message!.text!.split(' ');
	if (args.length <= 0) {
		await ctx.replyWithChatAction('typing');
		await ctx.reply('Emm... Qué es lo que debo decir? (・・ ) ?', { reply_to_message_id: ctx.message!.message_id });
		return;
	}

	await ctx.replyWithChatAction('typing');
	await ctx.reply(args.join(' '), {
		parse_mode: 'MarkdownV2',
		reply_to_message_id: ctx.message!.reply_to_message?.message_id,
	});

	let chatMember = await ctx.getChatMember(ctx.botInfo?.id ?? (await ctx.tg.getMe()).id);
	if (chatMember.can_delete_messages) {
		await ctx.deleteMessage(ctx.message!.message_id);
	}
});

export default General;
