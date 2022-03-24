data "aws_elb_service_account" "this" {}

resource "aws_s3_bucket" "logs" {
  bucket        = "elb-logs-devsu"
  acl           = "private"
  policy        = data.aws_iam_policy_document.logs.json
  force_destroy = true
}

data "aws_iam_policy_document" "logs" {
  statement {
    actions = [
      "s3:PutObject",
    ]

    principals {
      type        = "AWS"
      identifiers = "arn:aws:iam::647979279090:user/fercaceres"
    }

    resources = [
      "arn:aws:s3:::elb-logs-devsu/*",
    ]
  }
}

module "elb" {
  source = "../../"

  name = "elb-Dev-Ops"

  subnets         = ["subnet-018d3caa4b554f3c7","subnet-0936ccd222e5263c6"]
  security_groups = ["sg-0982a0590ce340569"]
  internal        = false

  listener = [
    {
      instance_port     = "5000"
      instance_protocol = "http"
      lb_port           = "8000"
      lb_protocol       = "http"
    },

  ]

  health_check_disable = true

  access_logs = {
    bucket = "elb-logs-devsu"
  }

  tags = {
    Owner       = "user"
    Environment = "dev"
  }

  # ELB attachments
  number_of_instances = 2
  instances           = ["i-03bc5ff999e929ab0","i-0776ed7ec56a99c4c"]
}

