from vk_api.keyboard import VkKeyboard, VkKeyboardColor

main_inline_keyboard = VkKeyboard(inline=True)
main_inline_keyboard.add_button("✳ Сдать батарейки", color=VkKeyboardColor.POSITIVE)
main_inline_keyboard.add_line()
main_inline_keyboard.add_button("✳ Сдать Раздельный мусор", color=VkKeyboardColor.NEGATIVE)
main_inline_keyboard.add_line()
main_inline_keyboard.add_button("✳ Сдать стекло", color=VkKeyboardColor.PRIMARY)
main_inline_keyboard.add_line()
main_inline_keyboard.add_button("✳ Сдать макулатуру", color=VkKeyboardColor.SECONDARY)

main_keyboard = VkKeyboard()
main_keyboard.add_button("📜 Главное меню", color=VkKeyboardColor.POSITIVE)

send_location = VkKeyboard(one_time=True)
send_location.add_location_button(payload=True)
