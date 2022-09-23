package views

import (
	"log"

	"github.com/Simeon2001/cloudfilm/box_gateway/request"
	"github.com/gofiber/fiber/v2"
)

func Upload_File(c *fiber.Ctx) error {
	get_file, err := c.FormFile("image")

	if err != nil {
		log.Println(err)
	}
	
	send, err := request.Post(get_file)

	return c.JSON(send)
	
}
