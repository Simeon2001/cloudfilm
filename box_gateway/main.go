package main

import (
	"github.com/Simeon2001/cloudfilm/box_gateway/views"
	"github.com/gofiber/fiber/v2"
	"fmt"
	"github.com/gofiber/fiber/v2/middleware/logger"
	"github.com/gofiber/fiber/v2/middleware/cors"
)

func helloworld(c *fiber.Ctx) error {
	fmt.Println("helloworld")
	return c.SendString("hello world boy mi")
}

func main() {
	app := fiber.New()
	app.Use(cors.New())
	app.Use(logger.New())
	app.Static("/images", "box_gateway/images")
	app.Get("/", helloworld)
	app.Post("/upload", views.Upload_File)
	app.Listen(":4000")
}
