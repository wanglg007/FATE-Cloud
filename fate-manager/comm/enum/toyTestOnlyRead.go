package enum

import "fate.manager/entity"

type ToyTestOnlyTypeRead int32

const (
	ToyTestOnlyTypeRead_UNKONWN ToyTestOnlyTypeRead = -1
	ToyTestOnlyTypeRead_YES     ToyTestOnlyTypeRead = 0
	ToyTestOnlyTypeRead_NO      ToyTestOnlyTypeRead = 1
)

func GetToyTestOnlyTypeReadString(p ToyTestOnlyTypeRead) string {
	switch p {
	case ToyTestOnlyTypeRead_YES:
		return "read"
	case ToyTestOnlyTypeRead_NO:
		return "no read"
	default:
		return "unknown"
	}
}

func GetToyTestOnlyTypeReadList() []entity.IdPair {
	var idPairList []entity.IdPair
	for i := 0; i < 2; i++ {
		idPair := entity.IdPair{i, GetToyTestOnlyTypeReadString(ToyTestOnlyTypeRead(i))}
		idPairList = append(idPairList, idPair)
	}
	return idPairList
}
