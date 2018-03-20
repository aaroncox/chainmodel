from chainmodel.models.steem import Block, Operation, OperationIndex
from chainmodel.models.steem.ops import *

class Schema():

    models = {
        'block': Block,
        'index': OperationIndex,
        'op': Operation,
        'ops': {
            'account_create': AccountCreate,
            'account_create_with_delegation': AccountCreateWithDelegation,
            'account_update': AccountUpdate,
            'account_witness_proxy': AccountWitnessProxy,
            'account_witness_vote': AccountWitnessVote,
            'author_reward': AuthorReward,
            'cancel_transfer_from_savings': CancelTransferFromSavings,
            'claim_reward_balance': ClaimRewardBalance,
            'comment': Comment,
            'comment_benefactor_reward': CommentBenefactorReward,
            'comment_options': CommentOptions,
            'curation_reward': CurationReward,
            'custom_json': CustomJSON,
            'custom_json_subtypes': {
                'follow': Follow,
                'reblog': Reblog,
            },
            'delegate_vesting_shares': DelegateVestingShares,
            'delete_comment': DeleteComment,
            'feed_publish': FeedPublish,
            'fill_order': FillOrder,
            'fill_transfer_from_savings': FillTransferFromSavings,
            'fill_vesting_withdraw': FillVestingWithdraw,
            'limit_order_cancel': LimitOrderCancel,
            'limit_order_create': LimitOrderCreate,
            'producer_reward': ProducerReward,
            'recover_account': RecoverAccount,
            'request_account_recovery': RequestAccountRecovery,
            'return_vesting_delegation': ReturnVestingDelegation,
            'set_withdraw_vesting_route': SetWithdrawVestingRoute,
            'transfer': Transfer,
            'transfer_from_savings': TransferFromSavings,
            'transfer_to_savings': TransferToSavings,
            'transfer_to_vesting': TransferToVesting,
            'vote': Vote,
            'witness_update': WitnessUpdate,
            'withdraw_vesting': WithdrawVesting,
        }
    }
