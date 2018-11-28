from typing import List, Optional

from telegram import Message


def extract_user_and_text(message: Message, args: List[str]) -> (Optional[int], Optional[str]):
    replied_message = message.reply_to_message
    
    if replied_message:
        user_id = replied_message.from_user.id
        reason = message.text.split(None, 1)

        if len(reason) < 2:
            return user_id, None
        
        return user_id, reason[1]
    else:
        return None, None
