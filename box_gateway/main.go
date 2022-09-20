package main

import (
	"github.com/gofiber/fiber/v2"
)

func helloworld(c *fiber.Ctx) error {
	return c.SendString("hello world")
}

func main() {
	app := fiber.New()
	app.Get("/", helloworld)
	app.Listen(":3000")
}
