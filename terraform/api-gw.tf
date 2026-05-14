resource "aws_apigateway2_api" "main" {
  name          = "equipment-sme"
  protocol_type = "HTTP"
}

resource "aws_apigateway2_integration" "aws_lambda" {
  api_id                 = aws_apigateway2_api.main.id
  integration_type       = "AWS_PROXY"
  integration_uri        = aws_lambda_function.main.invoke_arn
  payload_format_version = "2.0"
}

resource "aws_apigateway2_route" "post" {
  api_id    = aws_apigateway2_api.main.id
  route_key = "POST /sme-assistant"
  target    = "integrations/${aws_apigateway2_integration.aws_lambda.id}"
}

resource "aws_apigateway2_stage" "default" {
  api_id      = aws_apigateway2_api.main.id
  name        = "$default"
  auto_deploy = true
}
