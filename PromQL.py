class PromQL:
    
    def memory_total(): 
        memTotal = 'node_memory_MemTotal_bytes' + '{' + "instance=" + '"' + str("{}".format(self.instance)) + '"}' + ' offset ' + self.timeline
    
    def memory_free():    
        memFree  = 'node_memory_MemFree_bytes' + '{' + "instance=" + '"' + str("{}".format(self.instance)) + '"}' + ' offset ' + self.timeline
    
    def memory_buffers():
        memBuffers = 'node_memory_Buffers_bytes' + '{' + "instance=" + '"' + str("{}".format(self.instance)) + '"}' + ' offset ' + self.timeline

    def memory_cached():
        memCached = 'node_memory_Cached_bytes' + '{' + "instance=" + '"' + str("{}".format(self.instance)) + '"}' + ' offset ' + self.timeline

    def memory_sreclaimable(): 
        memSReclaimable = 'node_memory_SReclaimable_bytes' + '{' + "instance=" + '"' + str("{}".format(self.instance)) + '"}' + ' offset ' + self.timeline

    def memory_usage():
        node_memory_Usage_bytes = memory_total() + '-' + memory_free() + '-' + memory_buffers() + '-' + memory_cached() + '-' + memory_sreclaimable()
    
    def cpu_usage():
        node_cpu_Usage_bytes = 'avg by ' + "({})".format(self.instance) + '(irate(node_cpu_seconds_total{job="node",mode="idle"}' + '[' + self.timeline + ']' + '))'
