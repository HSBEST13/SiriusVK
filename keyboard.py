from vk_api.keyboard import VkKeyboard, VkKeyboardColor

blue, white, green, red = VkKeyboardColor.PRIMARY, VkKeyboardColor.SECONDARY, VkKeyboardColor.POSITIVE, \
                          VkKeyboardColor.NEGATIVE

main_pass_keyboard = VkKeyboard(inline=True)
main_pass_keyboard.add_button("✳ Сдать батарейки", color=green)
main_pass_keyboard.add_line()
main_pass_keyboard.add_button("✳ Сдать Раздельный мусор", color=red)
main_pass_keyboard.add_line()
main_pass_keyboard.add_button("✳ Сдать стекло", color=green)
main_pass_keyboard.add_line()
main_pass_keyboard.add_button("✳ Сдать макулатуру", color=red)
main_pass_keyboard.add_line()
main_pass_keyboard.add_button("✳ Сдать металл", color=green)

main_keyboard = VkKeyboard()
main_keyboard.add_button("📜 Главное меню", color=green)

main_inline_keyboard = VkKeyboard(inline=True)
main_inline_keyboard.add_button("✳ Сдать мусор", color=blue)
main_inline_keyboard.add_line()
main_inline_keyboard.add_button("✳ Эко - новости", color=green)
main_inline_keyboard.add_button("✳ Жалоба", color=red)

send_location = VkKeyboard(one_time=True)
send_location.add_location_button(payload=True)


list_keyboard = VkKeyboard(inline=True)
list_keyboard.add_button("⬅ Предыдущая новость", color=green)
list_keyboard.add_button("Следующая новость ➡", color=green)

bad_keyboard = VkKeyboard(one_time=True)
bad_keyboard.add_location_button(payload=True)
