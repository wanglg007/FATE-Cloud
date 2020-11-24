package app

import (
	"fate.manager/entity"
)

type CheckSystemResp struct {
	CommResp
	Data []entity.Prepare `json:"data"`
}

type AnsibleListResponse struct {
	CommResp
	Data entity.AnsibleList `json:"data"`
}

type AnsiblePackageResponse struct {
	CommResp
	Data []entity.AcquireRespItem `json:"data"`
}