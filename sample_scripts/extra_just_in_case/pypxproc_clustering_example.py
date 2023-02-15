import pypxproc
import traceback
dev = pixet.devices()[0]

def messageCb(error, msg):
    print("Message: {}, error={}".format(error, msg))

def progressCb(finished, progress):
    print("Progress: {}, finished={}".format(progress, finished))


def newClustersCb(clusters, acqIndex):
    try:
        print("NewClusters: size={},  acqIndex={}".format(len(clusters), acqIndex))
        for i in range(len(clusters)):
            cluster = clusters[i]
            print("Cluster: x={}, y={}, e={}, toa={}, size={}, height={}, id={}".format(
                   cluster.x, cluster.y, cluster.e, cluster.toa, cluster.size, cluster.height, cluster.id))
            for pix in cluster.pixels:
                print("  [{}, {}, {}, {}]".format(pix.x, pix.y, pix.e, pix.toa))
            if i > 50:
                break
    except:
        traceback.print_exc()


c = pypxproc.Clustering()
c.messageCallback = messageCb
c.progressCallback = progressCb
c.newClustersCallback = newClustersCb
c.newClustersWithPixelsCallback = newClustersCb

rc = c.replayData("somedata.t3pa", "", True)
print("Rc={}".format(rc))
