SRC =	groundhog.py

NAME =	groundhog

all:	$(NAME)

clean:
	@rm -f $(NAME)

$(NAME):	$(SRC)
	@cp $(SRC) $(NAME)
	@chmod 777 $(NAME)

fclean:	clean

re:	fclean all

.PHONY: all clean fclean re